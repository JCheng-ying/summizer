import argparse
import json

from src import graph_viz, pipeline


def main():
    parser = argparse.ArgumentParser(prog="summizer")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser(
        "init",
        help="首次运行:把当前 RSS 源里的文章全部标记为已读,不做分析(建立基线,避免第一次 check 处理几十篇历史文章)",
    )

    new_items_parser = sub.add_parser(
        "new-items", help="输出还没处理过的新文章(标题/链接/全文)为 JSON,供 Claude 阅读后撰写分析"
    )
    new_items_parser.add_argument("--limit", type=int, default=5)

    merge_parser = sub.add_parser(
        "merge-graph", help="把一篇文章的实体/关系抽取结果合并进持续积累的知识图谱,并标记该文章为已读"
    )
    merge_parser.add_argument("--item-file", required=True, help="new-items 输出中单篇文章对象的 JSON 文件路径")
    merge_parser.add_argument("--extraction-file", required=True, help="{entities:[...], relationships:[...]} 的 JSON 文件路径")

    mark_seen_parser = sub.add_parser("mark-seen", help="仅标记某篇文章为已读(不更新图谱),用于没有可抽取关系的文章")
    mark_seen_parser.add_argument("--url", required=True)
    mark_seen_parser.add_argument("--title", default="")

    sub.add_parser("graph", help="重新渲染知识图谱 HTML")

    args = parser.parse_args()

    if args.command == "init":
        count = pipeline.seed_baseline()
        print(f"[main] 基线建立完成,标记了 {count} 篇现有文章为已读,之后 new-items 只会返回更新的文章")

    elif args.command == "new-items":
        items = pipeline.get_new_items(limit=args.limit)
        print(json.dumps(items, ensure_ascii=False, indent=2))

    elif args.command == "merge-graph":
        with open(args.item_file, "r", encoding="utf-8") as f:
            item = json.load(f)
        with open(args.extraction_file, "r", encoding="utf-8") as f:
            extraction = json.load(f)
        pipeline.merge_graph(item, extraction)
        print(f"[main] 已合并进图谱并标记已读: {item['title']}")

    elif args.command == "mark-seen":
        from src import state

        state.mark_seen(args.url, args.title)
        print(f"[main] 已标记已读: {args.url}")

    elif args.command == "graph":
        path = graph_viz.render()
        print(f"[main] 图谱已重新生成: {path}")


if __name__ == "__main__":
    main()

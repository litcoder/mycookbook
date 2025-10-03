import sys
import frontmatter

if len(sys.argv) < 2:
    print(f"USAGE: {sys.argv[0]} <recipe_md>")
    exit(1)

recipe_file = sys.argv[1]
with open(recipe_file, "r") as f:
    # Metadata 추출
    post = frontmatter.load(f)
    metadata = post.metadata

    # 모든 메타데이타 출력
    for k, v in metadata.items():
        print(f"{k}: {v}")

title = input()
content = input()

print(f"<h1>")
print(f"    {title}")
print(f"</h1>")

print(f"<article>")
print(f"    {content}")
print(f"</article>")

comment = input()

while comment != "end of comments":
    print(f"<div>")
    print(f"    {comment}")
    print(f"</div>")
    comment = input()
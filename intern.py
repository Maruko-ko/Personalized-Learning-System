from graphviz import Digraph

dot = Digraph(comment="Prompt Engineering + RAG Flow", format="png")
dot.attr(rankdir="LR", size="8")

# Nodes
dot.node("A", "Student Profile\n(Level, Score, Experience, Target, Period)", shape="box", style="rounded,filled", fillcolor="lightblue")
dot.node("B", "Learning Materials\n(PDF/Text stored internally)", shape="folder", style="filled", fillcolor="white")
dot.node("C", "Chunking + Embedding\n(PyMuPDF + OpenAI Embeddings)", shape="box", style="rounded,filled", fillcolor="lightyellow")
dot.node("D", "Vector Database\n(pgvector)", shape="cylinder", style="filled", fillcolor="lightgrey")
dot.node("E", "Retrieve Relevant Chunks\n(based on profile & target)", shape="box", style="rounded,filled", fillcolor="lightyellow")
dot.node("F", "Prompt Engineering\n(Build full prompt with profile + chunks)", shape="box", style="rounded,filled", fillcolor="lightgreen")
dot.node("G", "OpenAI API\n(Generate learning plan)", shape="box", style="rounded,filled", fillcolor="palegreen")
dot.node("H", "Customised Learning Plan\n(JSON, multi-week)", shape="box", style="rounded,filled", fillcolor="lightblue")
dot.node("I", "Frontend UI\n(Display plan as timeline)", shape="box", style="rounded,filled", fillcolor="lightpink")

# Edges
dot.edge("A", "F", label="Student profile")
dot.edge("B", "C", label="Parse PDF")
dot.edge("C", "D", label="Store embeddings")
dot.edge("D", "E", label="Vector search")
dot.edge("A", "E", label="Goal keywords")
dot.edge("E", "F", label="Top-k chunks")
dot.edge("F", "G", label="Send prompt")
dot.edge("G", "H", label="Return plan")
dot.edge("H", "I", label="Show plan")

# Render
file_path = "/mnt/data/prompt_engineering_rag_flow"
dot.render(file_path, view=False)

file_path + ".png"

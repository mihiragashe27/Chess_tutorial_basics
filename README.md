# ♟️ Chess Beginner Guide & Interactive Board Engine

An Object-Oriented Python system designed to help beginner chess players bridge the gap between abstract algebraic notation (e.g., `Nf6`, `Qxd5`) and plain-English movement mechanics. 

Built from real-world chess coaching experience to eliminate friction points for new learners by linking algebraic move parsing with an interactive $8 \times 8$ matrix board model.

---

## 🌟 Key Features

### 1. Algebraic Move Translator
* **Natural Language Decoding:** Translates algebraic notations (`Nf6`, `Qxd5+`, `O-O`) into descriptive plain English (e.g., *"Knight moves to square f6"*).
* **Flag Handling:** Intercepts special actions including captures (`x`), checks (`+`), checkmates (`#`), and castling (`O-O` / `O-O-O`).
* **Piece Reference Guide:** Provides instant lookups for piece values (points) and movement mechanics using $O(1)$ dictionary lookups.

### 2. Object-Oriented Board Model (`ChessSquare`)
* **Matrix Representation:** Models an $8 \times 8$ chessboard using nested lists of `ChessSquare` instances.
* **Coordinate Mapping:** Keeps track of colors, ranks, and file columns to prepare for path validation and visual square highlighting.




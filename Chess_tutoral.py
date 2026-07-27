import sys


class ChessGuide:

  def __init__(self):
    # Dictionary storing piece values, names, and movement rules
    self.pieces_info = {
        "P": {
            "name": "Pawn",
            "value": 1,
            "movement": (
                "Moves forward 1 square (or 2 squares on its first move)."
                " Captures diagonally."
            ),
        },
        "N": {
            "name": "Knight",
            "value": 3,
            "movement": (
                "Moves in an 'L' shape (2 squares in one direction, then 1"
                " square perpendicular). Can jump over other pieces!"
            ),
        },
        "B": {
            "name": "Bishop",
            "value": 3,
            "movement": (
                "Moves diagonally any number of open squares, staying on its"
                " color."
            ),
        },
        "R": {
            "name": "Rook",
            "value": 5,
            "movement": (
                "Moves horizontally or vertically any number of open squares."
            ),
        },
        "Q": {
            "name": "Queen",
            "value": 9,
            "movement": (
                "Moves in any straight line—horizontally, vertically, or"
                " diagonally."
            ),
        },
        "K": {
            "name": "King",
            "value": "Infinite (Game Over if lost)",
            "movement": "Moves 1 square in any direction.",
        },
    }

    # Notation mapping dictionary
    self.notation_map = {
        "N": "Knight",
        "B": "Bishop",
        "R": "Rook",
        "Q": "Queen",
        "K": "King",
    }

  def show_piece_details(self, symbol):
    """Displays points, name, and movement for a selected piece."""
    symbol = symbol.upper()
    if symbol in self.pieces_info:
      info = self.pieces_info[symbol]
      print(f"\n--- {info['name'].upper()} ---")
      print(f"Points Value : {info['value']}")
      print(f"How it Moves : {info['movement']}")
    else:
      print("\nInvalid piece symbol! Use P, N, B, R, Q, or K.")

  def translate_notation(self, notation):
    """Translates standard algebraic notation (e.g., 'Nf6') into beginner plain text."""
    notation = notation.strip()

    # Handling Castling
    if notation == "O-O" or notation == "0-0":
      print("\nTranslation: King castles Kingside (short castle).")
      return
    elif notation == "O-O-O" or notation == "0-0-0":
      print("\nTranslation: King castles Queenside (long castle).")
      return

    # Check for capture, check, or checkmate symbols
    is_capture = "x" in notation
    is_check = "+" in notation
    is_checkmate = "#" in notation

    # Clean string to get clean destination square
    clean_notation = notation.replace("x", "").replace("+", "").replace("#", "")

    # Identify piece type
    first_char = clean_notation[0]
    if first_char in self.notation_map:
      piece_name = self.notation_map[first_char]
      target_square = clean_notation[1:]
    else:
      piece_name = "Pawn"
      target_square = clean_notation

    # Build plain English output
    action = "captures on" if is_capture else "moves to"
    result = f"\nTranslation: {piece_name} {action} square {target_square.lower()}."

    if is_checkmate:
      result += " (Checkmate! Game Over)"
    elif is_check:
      result += " (Puts opponent in Check!)"

    print(result)

  def start_app(self):
    """Runs the main menu loop."""
    while True:
      print("\n==========================================")
      print("   CHESS BEGINNER GUIDE & TRANSLATOR      ")
      print("==========================================")
      print("1. Look up Piece Values & Movement Rules")
      print("2. Translate Chess Notation to Plain English")
      print("3. Exit")

      choice = input("\nEnter your choice (1-3): ").strip()

      if choice == "1":
        print("\nSelect a Piece:")
        print("P: Pawn | N: Knight | B: Bishop | R: Rook | Q: Queen | K: King")
        piece = input("Enter piece symbol: ")
        self.show_piece_details(piece)

      elif choice == "2":
        move = input("\nEnter algebraic notation (e.g., Nf6, Qxd5, e4, O-O): ")
        self.translate_notation(move)

      elif choice == "3":
        print("\nThank you for using Chess Guide! Keep playing!")
        break
      else:
        print("\nInvalid choice! Please pick 1, 2, or 3.")


# --- RUN PROGRAM ---
if __name__ == "__main__":
  app = ChessGuide()
  app.start_app()

import chess

from cogs.libs.formatter import format_content

from cogs.libs.boards import boards


def legal_moves(_user_id):
    """
    shows possible legal moves.
    """
    _board = boards[_user_id]
    
    list_moves  = []
    for move in _board.legal_moves:
        list_moves.append(str(move))
    return format_content(", ".join(list_moves))


def legal_move(_user_id, _move):
    """
    checks whether it is a legal move.
    """
    _board = boards[_user_id]
    return chess.Move.from_uci(_move) in _board.legal_moves

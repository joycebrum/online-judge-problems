class Piece:
    def __init__(self, left = -1, right = -1, free = True):
        self.free = free
        self.left = left
        self.right = right

    def turn(self):
        temp = self.left
        self.left = self.right
        self.right = temp

    def __repr__(self):
        if self.free:
            return '[%s %s]' % (self.left, self.right)
        else:
            return '~%s %s~' % (self.left, self.right)

def can_use_piece(left, piece, right):
    if left.right == piece.left:
        if not right: return True
        if right.left == piece.right: return True
    return False

def can_use_turned_piece(left, piece, right):
    if left.right == piece.right:
        if not right: return True
        if right.left == piece.left: return True
    return False

def try_fill_board(left, pieces, right, placed_pieces, n):
    if placed_pieces == n-1:
        for piece in pieces:
            if piece.free:
                if can_use_piece(left, piece, right):
                    return True
                if can_use_turned_piece(left, piece, right):
                    piece.turn()
                    return True
        return False
    for piece in pieces:
        if piece.free:
            if can_use_piece(left, piece, None):
                piece.free = False
                if try_fill_board(piece, pieces, right, placed_pieces + 1, n):
                    return True
                piece.free = True
            elif can_use_turned_piece(left, piece, None):
                piece.free = False
                piece.turn()
                if try_fill_board(piece, pieces, right, placed_pieces + 1, n):
                    return True
                piece.free = True
    return False

if __name__ == '__main__':
    while True:
        n = int(input().strip())
        if n == 0:
            break
        m = int(input().strip())
        
        left_v = input().strip().split()
        left = Piece(int(left_v[0]), int(left_v[1]), False)
        
        right_v = input().strip().split()
        right = Piece(int(right_v[0]), int(right_v[1]), False)
        pieces = []
        for i in range(0, m):
            piece_v = input().strip().split()
            piece = Piece(int(piece_v[0]), int(piece_v[1]), True)
            pieces.append(piece)
        if try_fill_board(left, pieces, right, 0, n):
            print('YES')
        else:
            print('NO')


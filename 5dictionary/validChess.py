import pprint
chessPieces = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(checkBoard):
    # check if the black king and the white king are on the board
    # if they aren't, return false
    if 'bking' not in checkBoard.values() and 'wking' not in checkBoard.values():
        return False

    ## check if there are more than one of either king
    ## and that each player has at most 16 pieces
    ## and that each piece doesn't go out of bounds
    # count the number of white pieces
    whitePieces = 0
    # count the number of black pieces
    blackPieces = 0
    # count the number of white kings [max 1]
    whiteKing = 0
    # counte the number of black kings [max 1]
    blackKing = 0
    # count the number of white ponds [max 8]
    whitePonds = 0
    # count the number of black ponds [max 8]
    blackPonds = 0
    for position, piece in checkBoard.items():
        # load in the position number and position letter
        positionNumber = int(position[0])
        positionLetter = position[1]
        pieceColor = piece[0]
        pieceKind = piece[1:]

        # Check if the position of a piece is valid
        if not (positionNumber >= 1 and positionNumber <= 8 and positionLetter >= 'a' and positionLetter <= 'h'):
            print('position: ' + position + ', is invalid!')
            return False

        # validate white pieces
        elif pieceColor == 'w':
            whitePieces += 1
            if pieceKind == 'king':
                whiteKing += 1
                if whiteKing > 1:
                    print('White has more than one king!')
                    return False
            elif pieceKind == 'pond':
                whitePonds += 1
                if whitePonds > 8:
                    print('White has more than 8 ponds on the board!')
                    return False
            elif whitePieces > 16:
                print('White has more than 16 pieces on the board!')
                return False

        # validate black pieces
        elif pieceColor == 'b':
            blackPieces += 1
            if pieceKind == 'king':
                blackKing += 1
                if blackKing > 1:
                    print('Black has more than one king!')
                    return False
            elif pieceKind == 'pond':
                blackPonds += 1
                if blackPonds > 8:
                    print('Black has more than 8 ponds on the board!')
                    return False
            elif blackPieces > 16:
                print('Black has more than 16 pieces on the board!')
                return False
    if whiteKing == 0 and blackKing == 0:
        print('There is a missing king!')
        return False
    return True

print(isValidChessBoard(chessPieces))
            
        




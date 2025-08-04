import model
from model.model_name import KnightArena


@model.RequestSend(cmd=KnightArena.cmd, op=KnightArena.op)
def knight_arena():
    """华山论剑/挑战"""
    return


if __name__ == '__main__':
    for i in range(5):
        knight_arena()
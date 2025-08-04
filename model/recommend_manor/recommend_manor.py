import model
from model.model_name import RecommendManor


@model.RequestSend(cmd=RecommendManor.cmd, type=RecommendManor.type)
def recommend_manor_reward():
    """抢地盘/每日奖励"""
    return

if __name__ == '__main__':
    recommend_manor_reward()

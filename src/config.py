# 模型位置参数
MODEL_CK = "../models/cnn3_best_weights_ck.h5"
MODEL_JAFFE = "../models/cnn3_best_weights_jaffe.h5"
MODEL_FER = "../models/cnn3_best_weights_fer.h5"
# 日志等级参数
import os
"""
0：显示所有日志（默认级别）
1：显示警告和错误日志
2：只显示错误日志
3：只显示错误和致命日志
"""
LOG_LEVEL = os.environ["TF_CPP_MIN_LOG_LEVEL"]



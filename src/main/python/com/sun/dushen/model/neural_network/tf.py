import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from com.sun.dushen.common import utils

# 读取数据
df = utils.read_csv('hospital')

# 将日期列转换为 datetime 类型
df['日期'] = pd.to_datetime(df['日期'])

# 创建一个特征列，表示日期距离某个基准日期的天数
base_date = pd.to_datetime('20030223')
df['天数'] = (df['日期'] - base_date).dt.days

# 创建特征和目标变量
X = df[['天数']]
y = df['就诊量']

# 将数据拆分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特征标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 构建深度神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# 编译模型
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 训练模型
history = model.fit(X_train_scaled, y_train, epochs=100, validation_split=0.2)

# 评估模型
loss, mae = model.evaluate(X_test_scaled, y_test)

# 打印评估结果
print(f'Test Mean Absolute Error: {mae:.2f}')

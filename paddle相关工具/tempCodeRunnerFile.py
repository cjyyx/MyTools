net = paddle.nn.Sequential(
    paddle.nn.Linear(1, 8),
    paddle.nn.ReLU(),
    paddle.nn.Linear(8, 1),
    paddle.nn.Tanh()
)
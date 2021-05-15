import paddle
from control_parameters import *
from GD_fit import *




def eval(net):
    x=paddle.linspace(-3,3,100)
    x=paddle.reshape(x,[x.size,1])
    y=x**2
    loss_fn=paddle.nn.MSELoss(reduction='mean')
    loss=loss_fn(net(x),y)
    return loss

net = paddle.nn.Sequential(
    paddle.nn.Linear(1, 8),
    paddle.nn.ReLU(),
    paddle.nn.Linear(8, 1),
    paddle.nn.Tanh()
)

LR=0.1
dx=0.5

for b in range(100):
    for i in range(get_parameter_size(net)):
        loss=eval(net)
        para=get_parameter(net,i)
        set_parameter(net,i,para+dx)
        d_loss=eval(net)-loss
        if d_loss==0:
            continue
        grad=d_loss/dx
        new_pare=para-LR*(loss/grad)
        set_parameter(net,i,new_pare)

    if b%10==0:
        print(loss.numpy()[0])



import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# 我们可以往其中添加一些文本显示，或者在不同的条件下改变点样式。这其实也非常简单，
# 只需在update_points函数中添加一些额外的，你想要的效果代码即可。
# 我在上面update_points函数中添加了一个文本，让它显示点的(x, y)的坐标值，
# 同时在不同的帧，改变了点的形状，让它在5的倍数帧显示为五角星形状。

# def update_points(num):
#     if num % 5 == 0:
#         point_ani.set_marker("*")
#         point_ani.set_markersize(12)
#     else:
#         point_ani.set_marker("o")
#         point_ani.set_markersize(8)
#
#     point_ani.set_data(x[num], y[num])
#     text_pt.set_text("x=%.3f, y=%.3f" % (x[num], y[num]))
#     return point_ani, text_pt,


# 再稍微改变一下，可以让文本跟着点动。只需将上面的代码update_points函数改为如下代码，其效果如图2-4所示。
def update_points(num):
    point_ani.set_data(x[num], y[num])
    if num % 5 == 0:
        point_ani.set_marker("*")
        point_ani.set_markersize(12)
    else:
        point_ani.set_marker("o")
        point_ani.set_markersize(8)

    text_pt.set_position((x[num], y[num]))
    text_pt.set_text("x=%.3f, y=%.3f" % (x[num], y[num]))
    return point_ani, text_pt,


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig = plt.figure(tight_layout=True)
plt.plot(x, y)
point_ani, = plt.plot(x[0], y[0], "ro")
plt.grid(ls="--")
text_pt = plt.text(4, 0.8, '', fontsize=16)

ani = animation.FuncAnimation(
    fig, update_points, np.arange(0, 100), interval=100, blit=True)

# ani.save('sin_test3.gif', writer='imagemagick', fps=10)
plt.show()

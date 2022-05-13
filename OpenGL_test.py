# # Tutorial 1 : Opening a window
# # OpenGLとGLFWをimport
# from OpenGL.GL import *
# import glfw
#
#
# def main():
#     # GLFWの初期化
#     if not glfw.init():
#         raise RuntimeError('Failed to initialize GLFW')
#
#     # ウィンドウを作成
#     window = glfw.create_window(320, 240, 'OpenGL sample', None, None)
#     if not window:
#         glfw.terminate()
#         raise RuntimeError('Failed to create window')
#
#     # コンテキストを作成
#     glfw.make_context_current(window)
#
#     # ユーザがウィンドウを閉じるまでループ
#     while not glfw.window_should_close(window):
#         # ダブルバッファのスワップ
#         glfw.swap_buffers(window)
#
#         # イベントの受け付け
#         glfw.poll_events()
#
#     # ウィンドウを破棄
#     glfw.destroy_window(window)
#     # GLFWを終了
#     glfw.terminate()
#
#
# # メイン関数
# if __name__ == "__main__":
#     main()


# # Tutorial 2 : The first triangle
# import glfw
# from OpenGL.GL import *
# import OpenGL.GL.shaders
# import numpy
#
#
# def main():
#     # initialize glfw
#     if not glfw.init():
#         return
#
#     window = glfw.create_window(800, 600, "My OpenGL window", None, None)
#
#     if not window:
#         glfw.terminate()
#         return
#
#     glfw.make_context_current(window)
#     #            positions        colors
#     triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
#                 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
#                 0.0, 0.5, 0.0, 0.0, 0.0, 1.0]
#
#     triangle = numpy.array(triangle, dtype=numpy.float32)
#
#     vertex_shader = """
#     #version 330
#     in vec3 position;
#     in vec3 color;
#     out vec3 newColor;
#     void main()
#     {
#         gl_Position = vec4(position, 1.0f);
#         newColor = color;
#     }
#     """
#
#     fragment_shader = """
#     #version 330
#     in vec3 newColor;
#     out vec4 outColor;
#     void main()
#     {
#         outColor = vec4(newColor, 1.0f);
#     }
#     """
#     shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
#                                               OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
#
#     VBO = glGenBuffers(1)
#     glBindBuffer(GL_ARRAY_BUFFER, VBO)
#     glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)
#
#     position = glGetAttribLocation(shader, "position")
#     glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
#     glEnableVertexAttribArray(position)
#
#     color = glGetAttribLocation(shader, "color")
#     glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
#     glEnableVertexAttribArray(color)
#
#     glUseProgram(shader)
#
#     glClearColor(0.2, 0.3, 0.2, 1.0)
#
#     while not glfw.window_should_close(window):
#         glfw.poll_events()
#
#         glClear(GL_COLOR_BUFFER_BIT)
#
#         glDrawArrays(GL_TRIANGLES, 0, 3)
#
#         glfw.swap_buffers(window)
#
#     glfw.terminate()
#
#
# if __name__ == "__main__":
#     main()


# # OpenGLとGLFWをimport
# from OpenGL.GL import *
# import glfw
#
# def main():
#     # GLFWの初期化
#     if not glfw.init():
#         raise RuntimeError('Failed to initialize GLFW')
#
#     # ウィンドウを作成
#     window = glfw.create_window(320, 240, 'OpenGL sample', None, None)
#     if not window:
#         glfw.terminate()
#         raise RuntimeError('Failed to create window')
#
#     # コンテキストを作成
#     glfw.make_context_current(window)
#
#     # ユーザがウィンドウを閉じるまでループ
#     while not glfw.window_should_close(window):
#         # 線の色指定（赤）
#         glColor3f(1.0, 0.0, 0.0)
#         # 中を塗りつぶす
#         glBegin(GL_POLYGON)
#         glVertex2d(-0.9, -0.9)
#         glVertex2d(0.9, -0.9)
#         glVertex2d(0.9, 0.9)
#         glVertex2d(-0.9, 0.9)
#         glEnd()
#         # ダブルバッファのスワップ
#         glfw.swap_buffers(window)
#
#         # イベントの受け付け
#         glfw.poll_events()
#
#     # ウィンドウを破棄
#     glfw.destroy_window(window)
#     # GLFWを終了
#     glfw.terminate()
#
# # メイン関数
# if __name__ == "__main__":
#     main()


# # OpenGLとGLFWをimport
# from OpenGL.GL import *
# import glfw
#
# def main():
#     # GLFWの初期化
#     if not glfw.init():
#         raise RuntimeError('Failed to initialize GLFW')
#
#     # ウィンドウを作成
#     window = glfw.create_window(320, 240, 'OpenGL sample', None, None)
#     if not window:
#         glfw.terminate()
#         raise RuntimeError('Failed to create window')
#
#     # コンテキストを作成
#     glfw.make_context_current(window)
#
#     # ユーザがウィンドウを閉じるまでループ
#     while not glfw.window_should_close(window):
#         # 線の色指定（赤）
#         glColor3f(1.0, 0.0, 0.0)
#         # 線をつなぐ
#         glBegin(GL_LINE_LOOP)
#         glVertex2d(-0.9, -0.9)
#         glVertex2d(0.9, -0.9)
#         glVertex2d(0.9, 0.9)
#         glVertex2d(-0.9, 0.9)
#         glEnd()
#         # ダブルバッファのスワップ
#         glfw.swap_buffers(window)
#
#         # イベントの受け付け
#         glfw.poll_events()
#
#     # ウィンドウを破棄
#     glfw.destroy_window(window)
#     # GLFWを終了
#     glfw.terminate()
#
# # メイン関数
# if __name__ == "__main__":
#     main()


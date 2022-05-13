# Tutorial 1: Opening a Window

from __future__ import print_function
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GL.shaders import *
from glew_wish import *
import glfw
import sys


def main():
    # Initialize the library
    if not glfw.init():
        return

    # Open Window and create its OpenGL context
    window = glfw.create_window(800, 600, "Test_window", None, None)
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Initialize GLEW
    glfw.make_context_current(window)
    glfw.set_input_mode(window, glfw.STICKY_KEYS, True)

    # Loop until user closes the window
    while glfw.get_key(window, glfw.KEY_ESCAPE) != glfw.PRESS and not glfw.window_should_close(window):
        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()
    glfw.terminate()


if __name__ == "__main__":
    main()

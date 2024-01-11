from pyglet.graphics.shader import Shader, ShaderProgram


vert = """
#version 150 core
void main() {
  // Your vertex shader code here
}
"""

frag = """
#version 150 core
void main() {
  gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""


def useShaders():
  program = ShaderProgram(Shader(vert, 'vertex'), Shader(frag, 'fragment'))
  return program
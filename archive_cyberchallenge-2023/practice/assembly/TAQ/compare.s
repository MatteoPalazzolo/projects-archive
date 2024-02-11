func:
  cmp rdi, rsi
  jge greater1
  mov rax, rsi
  jmp end1

greater1:
  mov rax, rdi
  jmp end1

end1:
  cmp rdx, rax
  jg greater2
  jmp end2

greater2:
  mov rax, rdx
  jmp end2

end2:
  ret
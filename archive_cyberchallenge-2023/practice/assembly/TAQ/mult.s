func:
  mov rbx, rdi
  shr rdi, 2
  mov rax, rdi
  shl rdi, 2
  sub rbx, rdi
  cmp rbx, 2
  jle end1
  jmp end2

end1:
  shl rax, 2
  ret

end2:
  add rax, 1
  shl rax, 2
  ret


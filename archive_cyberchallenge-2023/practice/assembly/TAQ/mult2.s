func:
  mov eax, edi
  mov ebx, 4
  div ebx
  cmp edx, 2
  jle end1
  jmp end2

end1:
  mul ebx
  ret

end2:
  add eax, 1
  mul ebx
  ret
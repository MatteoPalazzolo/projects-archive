; nasm -f elf64 -o gpt.o gpt.asm && ld -o gpt gpt.o

section .data
  format db "sum: %d", 10, 0

section .text

global _start, sum
extern printf

_start:
    ; call our sum function with arguments 2, 4, and 6
    mov rdi, 2
    mov rsi, 4
    mov rdx, 6
    call sum
    
    mov rdi, format
    mov rsi, rax
    xor rax, rax
    call printf

    ; exit the program
    mov rax, 60      ; system call for exit
    xor rdi, rdi     ; exit code 0
    syscall

sum:
    ; function prologue - save the base pointer and allocate stack space
    ; push rbp
    ; mov rbp, rsp
    ; sub rsp, 8      ; allocate 8 bytes for local variables

    ; add the three arguments together
    mov rax, rdi
    add rax, rsi
    add rax, rdx

    ; function epilogue - restore the base pointer and return the sum
    ; mov rsp, rbp
    ; pop rbp
    ret

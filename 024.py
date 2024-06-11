#Escreva um programa que peça ao usuário uma senha e verifique se ela está correta (a senha correta é "python123").

print('Olá, este é o seu banco digital!')
senhaCorreta = 'python123'

senhaUsuario = input('Digite a senha: ').strip()

if senhaUsuario == senhaCorreta:
    print('Senha correta! Seja bem vindo')

else:
    print('[ERRO} A senha está incorreta!')
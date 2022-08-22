from datetime import datetime

from videogame import VideoGame, MarcaInvalida, HdInvalido

if __name__ == '__main__':
    print(VideoGame.__module__)
    xbox = VideoGame("05/02/2022", "XBOX", "360")
    xbox.instalar_jogo("FIFA 2022")
    xbox.instalar_jogo("PES 2022")
    print(xbox)
    print(xbox.__dict__)
    print(xbox.get_jogos_instalados())
    print("---")
    print(VideoGame.__name__)
    print("---")
    print(hasattr(xbox, 'hahahaha'))
    xbox.hahahaha = 123
    print(hasattr(xbox, 'hahahaha'))

    ps4 = VideoGame()
    try:
        ps4.marca = "Playstation"
        ps4.modelo = "4 Slim"
        ps4.hd = 1024
        print(ps4)
    except MarcaInvalida as m:
        print(m.args[0], m.args[1])
    except HdInvalido as m1:
        print(m1.args[0])
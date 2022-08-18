from datetime import datetime

from videogame import VideoGame

if __name__ == '__main__':
    print(VideoGame.__module__)
    xbox = VideoGame(datetime.strptime("05/02/2022", "%d/%m/%Y"), "XBOX", "360")
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
    ps4.marca = "Playstation"
    ps4.modelo = "4 Slim"
    print(ps4)
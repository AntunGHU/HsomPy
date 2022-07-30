# 1'12

# otvaranje browsera iz py-scripte. Posebno korisno ako gradimo automatizacijsku skriptu koja radi gomilu zadataka i na kraju zelimo otvoriti browser-window
# npr, gradimo skriptu za deplore our web site kojeg gradimo na nasoj lokalnoj masini. Kad zavrsimo zelimo pokrenuti ovu skriptu i deplojati nas posao na web-server
# na kraju cemo morati otvoriti browser-window, manualno ukucati url naseg web-sajta i klik na Enter. Ovi koraci su rucni i mogu se automatizirati!!!
import webbrowser
print("Deployment completed!")
webbrowser.open(
    "https://www.youtube.com/channel/UC1qkMXH8d2I9DDAtBSeEHqg/videos")
# ako ranamo skriptu : ispisuje se print i otvara stranica!!!

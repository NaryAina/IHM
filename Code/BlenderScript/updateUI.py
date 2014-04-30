# Updates the UI information
#

from bge import logic as gl

scn = gl.getCurrentScene()
obl = scn.objects

obl["UIscore"].text = "WHAT"
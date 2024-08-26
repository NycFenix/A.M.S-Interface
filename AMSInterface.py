from lib.ui import Ui_AMS_Interface
from include import BeadGeometry


class AMSInterface(Ui_AMS_Interface):
    def __init__(self):
        super(AMSInterface, self).__init__()
        self.setupUi(self)

    













def GeometricPredictionCallback(self, Ws, Ts, V, I, Mp, Sh, Vi, De, Ct, D):
        penetration = BeadGeometry.getPenetration(V, I, Ws, Ts, Mp, Sh)
        #t_solid = BeadGeometry.getT_Sol(Sh, D, Ts, I, V, De, penetration, Mp, Ct, Ws)
        t_solid = 0.8 #Valor temporário
        height, width = BeadGeometry.getBeadGeometry(D, Ws, Ts, I, V, t_solid, De, Sh, Vi, Ct)
        
        self.penetration.setText(str(round(penetration, 3)))
        self.t_solid.setText(str(round(t_solid,3)))
        self.height.setText(str(round(height,3)))
        self.width.setText(str(round(width,3)))


def SpeedMeasureConverter(self, speed = str,flag = int):
    #This method converts mm/s into m/min and vice-versa
    # If flag = 1, mm/s -> m/min
    # if its -1, m/min -> mm/s

    try:
        speed = float(speed)
        new_speed  = speed * ((60 / 1000) ** flag)
        return str(round(new_speed, 3))
    except ValueError: # If nothing is written or input is invalid, does not convert
        return ""

def DeltaECallback(self, deltaE = str):
    try:
        deltaE = float(deltaE)
        deltaE = BeadGeometry.getDeltaE(deltaE)
        return str(round(deltaE, 3))
    except ValueError:
        return ""
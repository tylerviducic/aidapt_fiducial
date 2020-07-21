# module for checking if event passes fiducial cut

class FiducialCuts:

    def __init__(self):
        self.phi_cut = 0.0
        self.theta_cut = 0.0
        self.momentum_cut = 0.0

    def check_if_pass(self, event):
        return True


    # Private methods

    def _passes_phi(self, phi):
        return phi > self.phi_cut

    def _passes_theta(self, theta):
        return theta > self.theta_cut

    def _passes_momentum(self, momentum):
        return momentum > self.momentum_cut
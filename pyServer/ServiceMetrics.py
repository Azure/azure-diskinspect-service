#!/usr/bin/python3

"""
Health Metrics 
"""
class ServiceMetrics:

    TotalRequests = None
    SuccessRequests = None
    TotalSuccessServiceTime = None
    ActiveRequests = None
    ConsecutiveErrors = None

    def __init__(self):
        self.TotalRequests = 0
        self.SuccessRequests = 0
        self.TotalSuccessServiceTime = 0
        self.ActiveRequests = 0
        self.ConsecutiveErrors = 0

    def getMetrics(self):
        if (self.SuccessRequests > 0):
            avgSuccessServiceTime = self.TotalSuccessServiceTime / self.SuccessRequests
        else:
            avgSuccessServiceTime = 0

        resultStr = 'Total Requests: ' + str(self.TotalRequests) + \
                    ', Success Requests: ' + str(self.SuccessRequests) + \
                    ', Avg Success Service Time: ' + str(avgSuccessServiceTime) + 's' \
                    ', Active Requests: ' + str(self.ActiveRequests) + \
                    ', Consecutive Errors: ' + str(self.ConsecutiveErrors)
        return resultStr
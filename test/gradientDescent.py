#class GradientDescent {
#
#    fun calculate(d: (Double) -> Double, start: Double, epsilon: Double, minStep: Double): Double {
#
#        var x = start
#
#        var step = 2 * minStep
#
#        while (abs(step) > minStep) {
#            val y = d.invoke(x)
#            step = epsilon * y
#            x -= step
#        }
#
#        return x
#    }
#
#}


def calculate(d, start, epsilon, minStep):
    x = start
    step = 2*minStep

    while(abs(step) > minStep):
        y = d(x)
        step = epsilon * y
        x = x - step

    return x

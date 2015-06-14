from factors import *

if __name__ == '__main__':
    # Trav is t
    # Fraud is f
    # OC is c
    # CRP is p
    # FP is a
    # IP is i
    travel = Factor('t',
            (((True,), 0.05),
             ((False,), 0.95)))

    computer_owner = Factor('c',
            (((True,), 0.75),
             ((False,), 0.25)))

    fraud = Factor('ft',
            (((True, True), 0.01),
             ((False, True), 0.99),
             ((True, False), 0.004),
             ((False, False), 0.996)))

    computer_buy = Factor('pc',
            (((True, True), 0.1),
             ((False, True), 0.9),
             ((True, False), 0.001),
             ((False, False), 0.999)))

    foreign_buy = Factor('atf',
            (((True, False, True), 0.1),
             ((False, False, True), 0.9),
             ((True, True, True), 0.9),
             ((False, True, True), 0.1),
             ((True, True, False), 0.9),
             ((False, True, False), 0.1),
             ((True, False, False), 0.01),
             ((False, False, False), 0.99)))

    i_buy = Factor('icf',
            (((True, False, True), 0.011),
             ((False, False, True), 0.989),
             ((True, True, True), 0.02),
             ((False, True, True), 0.98),
             ((True, True, False), 0.01),
             ((False, True, False), 0.99),
             ((True, False, False), 0.001),
             ((False, False, False), 0.999)))

    hidden_order = 'taficp'
    print(inference(
        [travel, fraud, computer_owner, computer_buy, foreign_buy, i_buy],
        'taicp', []))

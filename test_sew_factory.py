import sew_factory

# TESTCASES
# ================== uneven t-shirts ================== #

# a. uneven machines with more uneven t-shirts:
def test_a():
    assert sew_factory.get_time_to_create_tshirt(1, 9) == 45.0
    assert sew_factory.get_time_to_create_tshirt(3, 9) == 15.0
    assert sew_factory.get_time_to_create_tshirt(5, 9) == 10.0

# b. uneven machines with less uneven t-shirts:
def test_b():
    assert sew_factory.get_time_to_create_tshirt(13, 9) == 5.0
    assert sew_factory.get_time_to_create_tshirt(15, 9) == 5.0
    assert sew_factory.get_time_to_create_tshirt(17, 9) == 5.0

# c. even machines with more uneven t-shirts:
def test_c():
    assert sew_factory.get_time_to_create_tshirt(2, 9) == 25.0
    assert sew_factory.get_time_to_create_tshirt(6, 9) == 10.0
    assert sew_factory.get_time_to_create_tshirt(8, 9) == 10.0

# d. even machines with less uneven t-shirts:
def test_d():
    assert sew_factory.get_time_to_create_tshirt(12, 9) == 5.0
    assert sew_factory.get_time_to_create_tshirt(16, 9) == 5.0
    # doubling the workload (twice as fast)
    assert sew_factory.get_time_to_create_tshirt(18, 9) == 2.5

# ==================== even t-shirts ================== #

# e. uneven machines with more even t-shirts:
def test_e():
    assert sew_factory.get_time_to_create_tshirt(1, 10) == 50.0
    assert sew_factory.get_time_to_create_tshirt(3, 10) == 20.0
    assert sew_factory.get_time_to_create_tshirt(5, 10) == 10.0

# f. uneven machines with less even t-shirts:
def test_f():
    assert sew_factory.get_time_to_create_tshirt(13, 10) == 5.0
    assert sew_factory.get_time_to_create_tshirt(15, 10) == 5.0
    assert sew_factory.get_time_to_create_tshirt(17, 10) == 5.0

# g. even machines with more even t-shirts:
def test_g():
    assert sew_factory.get_time_to_create_tshirt(2, 10) == 25.0
    assert sew_factory.get_time_to_create_tshirt(6, 10) == 10.0
    assert sew_factory.get_time_to_create_tshirt(8, 10) == 10.0

# h. even machines with less uneven t-shirts:
def test_h():
    assert sew_factory.get_time_to_create_tshirt(12, 10) == 5.0
    assert sew_factory.get_time_to_create_tshirt(16, 10) == 5.0
    assert sew_factory.get_time_to_create_tshirt(18, 10) == 5.0

# ===================================================== #

# i. misc
def test_i():

    # same amount of machines and t-shirts
    assert sew_factory.get_time_to_create_tshirt(20, 20) == 5.0
    assert sew_factory.get_time_to_create_tshirt(35, 35) == 5.0
    assert sew_factory.get_time_to_create_tshirt(122, 122) == 5.0

    # twice as fast (double workload)
    assert sew_factory.get_time_to_create_tshirt(100, 23) == 2.5
    assert sew_factory.get_time_to_create_tshirt(200, 23) == 2.5

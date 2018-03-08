def test_basic_counter():
    # Starts with 0
    Cookie.count() == 0

    # We create 2 cookies
    c = Cookie()
    c = Cookie()

    # Now counter == 2
    Cookie.count() == 2

    # We now reset the counter
    Cookie.reset_counter()

    # Count is back to 0
    Cookie.count() == 0

    # But if we create a few more cookies:

    c = Cookie()
    c = Cookie()
    c = Cookie()
    c = Cookie()

    # Counter is still counting
    Cookie.count() == 4

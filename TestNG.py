import pytest

# ---------- Setup & Teardown (Similar to BeforeClass/AfterClass in TestNG) ----------
@pytest.fixture(scope="module", autouse=True)
def setup_module():
    print("\n[Setup for module]")
    yield
    print("\n[Teardown for module]")

@pytest.fixture(autouse=True)
def setup_each():
    print("\n---> Before each test")
    yield
    print("---> After each test")

# ---------- 1. Assertions ----------
def test_assertion_example():
    assert 5 == 5
    assert "hello".upper() == "HELLO"

# ---------- 2. Skip / Ignore ----------
@pytest.mark.skip(reason="Test is temporarily disabled")
def test_skip_example():
    assert False  # This won't run

# ---------- 3. Priority via naming (pytest doesn’t have native priority) ----------
def test_a_first():
    print("Runs first by name")

def test_b_second():
    print("Runs second by name")

# ---------- 4. Dependent Test ----------
@pytest.mark.dependency()
def test_login():
    print("Login Successful")
    assert True

@pytest.mark.dependency(depends=["test_login"])
def test_dashboard():
    print("Dashboard loaded after login")
    assert True

# ---------- 5. Repeat test using invocation count ----------
@pytest.mark.parametrize("run", range(3))
def test_run_multiple_times(run):
    print(f"Test run #{run+1}")

# ---------- 6. Parameterized Test ----------
@pytest.mark.parametrize("username, password", [
    ("admin", "admin123"),
    ("user", "user123")
])
def test_login_param(username, password):
    print(f"Testing with Username: {username} and Password: {password}")
    assert username != "" and password != ""

# ---------- 7. Data Driven Testing ----------
@pytest.mark.parametrize("data", [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 90}
])
def test_data_driven(data):
    print(f"Student: {data['name']}, Score: {data['score']}")
    assert data["score"] >= 0

# ---------- 8. Grouping Tests ----------
@pytest.mark.smoke
def test_smoke_case():
    print("Smoke Test")

@pytest.mark.regression
def test_regression_case():
    print("Regression Test")

@pytest.mark.sanity
def test_sanity_case():
    print("Sanity Test")

# ---------- 9. Parallel Testing Compatible (via pytest-xdist) ----------
def test_parallel_1():
    print("Parallel Test 1")

def test_parallel_2():
    print("Parallel Test 2")

# ---------- 10. Skipping conditionally ----------
@pytest.mark.skipif(2 > 1, reason="Just a demo conditional skip")
def test_conditional_skip():
    assert True

import subprocess

def test_dut_ssh():

    result = subprocess.run(
        ["ssh", "admin@10.16.9.109", "hostname"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    assert result.returncode == 0
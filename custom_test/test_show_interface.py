import subprocess


def test_show_interface_status():

    result = subprocess.run(
        ["ssh", "admin@10.16.9.109", "show interface status"],
        capture_output=True,
        text=True
    )

    print("\nCOMMAND OUTPUT:\n")
    print(result.stdout)

    assert result.returncode == 0
    assert "Interface" in result.stdout
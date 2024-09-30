rule TestRule {
    meta:
        description = "A simple test rule to detect the string 'malware_test'"
        author = "Your Name"
        date = "2024-09-28"
        version = "1.0"

    strings:
        $test_string = "malware_test"

    condition:
        $test_string
}

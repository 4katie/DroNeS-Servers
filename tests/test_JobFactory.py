import json
import os
import unittest
from jsonschema import validate
from Scheduling.JobFactory import JobFactory


class mockArgs:
    def __init__(self):
        self.job_items = [
            {
                "item": "mock_item",
                "reward": [0, 0],
                "penalty": [0, 0],
                "valid_for": [0, 0],
            }
        ]
        self.origin = [0, 0]
        self.radius = 3000
        self.generator_params = 0.1


def load_schema(filename):
    file = os.path.join(os.path.dirname(__file__), "schemas/" + filename)
    with open(file) as f:
        return json.loads(f.read())


class JobFactoryTest(unittest.TestCase):
    def setUp(self):
        self.args = mockArgs()
        self.factory = JobFactory(self.args)

    def testGenerateJob(self):
        job = self.factory.generateJob()
        self.assertTrue(job is not None)

    def testJobSchema(self):
        schema = load_schema("job.json")
        job = self.factory.generateJob()
        # we'll serialise the cost function before validating
        job["cost_function"] = job["cost_function"].__dict__
        validate(job, schema)


if __name__ == "__main__":
    unittest.main()

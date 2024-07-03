import kue from "kue";
import createPushNotificationsJobs from './8-job.js';
import { expect } from "chai";
import { describe } from "mocha";

const queue = kue.createQueue();
// write a test suite for the function 
// use expect.testMode to validate which jobs are in the queue
const list = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  }
];
describe("createPushNotificationsJobs", () => {
  it("validates the jobs are in the queue", () => {

    createPushNotificationsJobs(list, queue);
    expect(queue.testMode.jobs.length).to.equal(+0);
  });
  it("Create two new jobs to the queue", () => {
    createPushNotificationsJobs(list, queue);
    createPushNotificationsJobs(list, queue);
  });
})



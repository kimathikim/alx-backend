#!/usr/bin/env node
// create a job using kue
import kue from "kue"
const queue = kue.createQueue();
// array of blacklisted phone numbers
const blacklisted = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  // track progress from 0 to 100
  job.progress(0, 100);
  if (blacklisted.includes(phoneNumber)) {
    return done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

queue.process("push_notification_code_2", (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
  done();
});


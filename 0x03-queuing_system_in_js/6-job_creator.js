import { kue } from "kue";

const queue = kue.createQueue();

obj = {
  phoneNumber: string,
  message: string,
};

job = queue.create("push_notification_code", obj).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

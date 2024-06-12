import kue from "kue";

const queue = kue.createQueue();

const obj = {
  phoneNumber: '07949392929',
  message: "You are doing great!"
};

const job = queue.create("push_notification_code", obj).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on("complete", () => {
  console.log("Notification job completed");
});
job.on("failed", () => {
  console.log("Notification job failed");
});

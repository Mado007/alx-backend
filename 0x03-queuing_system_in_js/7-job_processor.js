const kue = require("kue");

const blacklist = ["4153518780", "4153518781"];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  } else {
    job.progress(50, 100);
    console.log(
      `Sending notification to ${phoneNumber}, with message: ${message}`
    );
    done()
  }
};

const queue = kue.createQueue();

queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});

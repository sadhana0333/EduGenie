// =========================================================
// EDU GENIE - JAVASCRIPT
// =========================================================


// ---------------------------------------------------------
// Q&A QUICK QUESTION
// ---------------------------------------------------------

function setQuestion(question) {

    const questionBox = document.getElementById("question");

    if (questionBox) {

        questionBox.value = question;

        questionBox.focus();

    }
}


// ---------------------------------------------------------
// EXPLAIN TOPIC QUICK BUTTON
// ---------------------------------------------------------

function setTopic(topic) {

    const topicBox = document.getElementById("topic");

    if (topicBox) {

        topicBox.value = topic;

        topicBox.focus();

    }
}


// ---------------------------------------------------------
// QUIZ QUICK TOPIC
// ---------------------------------------------------------

function setQuizTopic(topic) {

    const topicBox = document.getElementById("topic");

    if (topicBox) {

        topicBox.value = topic;

        topicBox.focus();

    }
}


// ---------------------------------------------------------
// PAGE LOAD
// ---------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {

    console.log("EduGenie loaded successfully!");

});
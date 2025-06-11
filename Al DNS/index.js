import { startUdpServer, createResponse, createTxtAnswer } from 'denamed';
import { GoogleGenerativeAI } from "@google/generative-ai";

const GEMINI_API_KEY = ""; // add the api key 

const genAI = new GoogleGenerativeAI(GEMINI_API_KEY); 
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" }); 

startUdpServer(async (query) => { 
    const question = query.question[0];
    console.log('Question:', question); // Fixed typo (`comsole` → `console`)
    
    const prompt = `Answer the question in one word or sentence. Question: ${question.name.split('.').join(' ')}`;
    const result = await model.generateContent(prompt);
    const response = await result.response; // Extract response text
    const answer = response.text(); // Get the generated answer

    return createResponse({ 
        query, 
        answers: [createTxtAnswer(question, answer)] // Use AI response instead of 'hello world'
    });
}, { port: 8000 });
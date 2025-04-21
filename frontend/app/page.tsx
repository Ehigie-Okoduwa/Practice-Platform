// Purpose: Create a welcoming landing page for students to start practicing
// Inpput: Greeting, form with course and topic inputs, Tailwind CSS for monochrome styling
// Output: A clean, black-and-white page with a heading, form, and button
// Logic: Use Tailwind classes for layout and styling, add a form with inputs and a button, ensure mobile-first design

import React from 'react'; 

export default function Home(){
  return (
    <div className="min-h-screen bg-white flex flex-col items-center justify-center p-4">
      {/* Greeting Section */}
      <h1 className="text-3xl font-bold text-black mb-2">Welcome to Practice Platform!</h1>
      <h2 className="text-lg text-black mb-6">What would you like to practice today?</h2>

      {/* Form Section */}
      <form className="w-full max-w-md flex flex-col gap-6">
        <p className="text-black text-sm mb-2">
          Fill this out for tailored Practice
        </p>
        <div>
          <label htmlFor="course" className="block text-black text-base mb-1">
            Course Name
          </label>
          <input 
            type="text"
            id="course"
            placeholder="e.g., Math 114"
            className="w-full p-2 border border-black rounded text-black placeholder-gray-500"
          />
        </div>
        <div>
          <label htmlFor="topic" className="block text-black text-base mb-1">
            Topic
          </label>
          <input 
            type="text"
            id="topic"
            placeholder="e.g., Quadratics or upload a file later"
            className="w-full p-2 border border-black rounded text-black placeholder-gray-500"
          />
        </div>
        <div className="flex flex-col items-center gap-2">
          <button
            type="submit"
            className="bg-black text-white py-3 px-6 rounded hover:bg-gray-800 text-lg font-semibold"
          >
            Start Practicing
          </button>
          
        </div>
      </form>
    </div>
  );
}
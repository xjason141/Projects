import React from "react";
import "./Profile.css";

function Hello() {
  const edu = [
    "Software Engineer Trainee",
    "Google IT Automation with Python",
    "Bachelor of Islamic Finance and Banking with Honours",
  ];
  const show_edu = edu.map((eduInfo) => (
    <li key={crypto.randomUUID()}>{eduInfo}</li>
  ));

  const eduDesc = [
    "- K-Youth (TalentLabs)",
    "- Coursera",
    "- Universiti Utara Malaysia",
  ];
  const show_desc = eduDesc.map((descInfo) => (
    <li key={crypto.randomUUID()}>{descInfo}</li>
  ));

  return (
    <>
      <h1 className="name">MUHAMMAD HAMDI HAMIZAN BIN YAZID</h1>
      <h2 className="headers">Career Objective</h2>
      <p className="intro">
        A motivated and eager-to-learn programmer skilled in HTML5, JavaScript
        and Python. I am currently seeking an entry-level programmer position to
        begin my journey as a Python developer. Able and open to learning new
        languages. My main objective is to create software that can be benefited
        by the public.
      </p>
      <h2 className="headers">Education History</h2>
      <ul className="eduList">{show_edu}</ul>
    </>
  );
}

// export default function MyApp() {
//     return (
//         <Hello/>
//     )
// }

export default Hello;

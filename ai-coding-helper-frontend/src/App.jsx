// src/App.jsx
import React, { useState } from 'react';
import MonacoEditor from '@monaco-editor/react';
import axios from 'axios';
import './App.css'

function App() {
    const [code, setCode] = useState('');
    const [suggestion, setSuggestion] = useState('');

    const handleEditorChange = (newValue) => {
        setCode(newValue);
    };

    const getSuggestion = async () => {
        const response = await axios.post('http://localhost:3000/suggest-code', { code });
        setSuggestion(response.data.suggestion);
    };

    return (
        <div>
            <MonacoEditor
                height="600px"
                language="javascript"
                theme="vs-dark"
                value={code}
                onChange={(value) => handleEditorChange(value)}
            />
            <button onClick={getSuggestion}>Get Suggestion</button>
            <div>Suggestion: {suggestion}</div>
        </div>
    );
}

export default App;

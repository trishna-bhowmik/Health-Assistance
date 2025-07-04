import React, { useState, useRef, useEffect } from 'react';
import { api } from '../api';
import { useAuth } from '../authContext';
import { useNavigate } from 'react-router-dom';

const Chat = () => {
  const { token, logout } = useAuth();
  const navigate = useNavigate();
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    if (!token) {
      navigate('/login');
    }
  }, [token, navigate]);

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    const userMsg = {
      sender: 'user',
      text: input,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      const res = await api.post('/ask', { question: input });
      const botMsg = {
        sender: 'bot',
        text: res.data.answer,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, botMsg]);
    } catch (err) {
      setMessages(prev => [...prev, {
        sender: 'bot',
        text: '⚠️ Error. Please try again later.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }]);
    } finally {
      setIsLoading(false);
    }
  };
  
  useEffect(() => {
  const loadHistory = async () => {
    try {
      const res = await api.get('/history', {
        headers: { Authorization: `Bearer ${token}` }
      });
      const loaded = res.data.map(h => ({
        sender: 'user+bot',
        question: h.question,
        answer: h.answer,
        timestamp: new Date(h.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }));
      const formatted = loaded.flatMap(item => [
        { sender: 'user', text: item.question, timestamp: item.timestamp },
        { sender: 'bot', text: item.answer, timestamp: item.timestamp }
      ]);
      setMessages(formatted);
    } catch (err) {
      console.error('Error loading history:', err);
    }
  };

  if (token) loadHistory();
}, [token]);

  return (
    <div className="bg-gradient-to-tr from-green-50 to-green-100 min-h-screen flex items-center justify-center px-4">
      <div className="w-full max-w-4xl h-[90vh] shadow-2xl rounded-lg bg-white flex flex-col border border-gray-300 overflow-hidden">
        <header className="bg-green-600 text-white text-center py-4 shadow-md flex justify-between px-6 items-center">
          <h1 className="text-xl font-bold">🩺 Health Assistant</h1>
          <button onClick={logout} className="text-sm bg-white text-green-600 px-3 py-1 rounded hover:bg-green-100">
            Log Out
          </button>
        </header>

        <div className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
          {messages.map((msg, i) => (
            <div key={i} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`flex flex-col max-w-[75%] text-sm ${msg.sender === 'user' ? 'items-end' : 'items-start'}`}>
                <div className={`px-4 py-2 rounded-2xl shadow-md ${
                  msg.sender === 'user'
                    ? 'bg-green-500 text-white rounded-br-none'
                    : 'bg-gray-200 text-gray-800 rounded-bl-none'
                }`}>
                  {msg.text}
                </div>
                <span className="text-xs text-gray-400 mt-1">{msg.timestamp}</span>
              </div>
            </div>
          ))}
          {isLoading && (
            <div className="flex justify-start">
              <div className="bg-gray-200 text-gray-600 px-4 py-2 rounded-2xl text-sm shadow-sm">
                Typing...
              </div>
            </div>
          )}
          <div ref={chatEndRef} />
        </div>

        <div className="flex items-center p-4 border-t border-gray-300 bg-white">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Type your question..."
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-400 text-sm"
          />
          <button
            onClick={sendMessage}
            className="ml-3 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 disabled:bg-green-300 text-sm"
            disabled={isLoading}
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chat;

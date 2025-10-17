import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

fetch("http://localhost:8000/api/hello")
  .then(res => res.json())
  .then(data => console.log(data));
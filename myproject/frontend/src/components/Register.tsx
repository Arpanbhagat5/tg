import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";

interface PrefectureChoice {
  value: string;
  display_name: string;
}

interface RegisterFormData {
  username: string;
  email: string;
  password: string;
  tel?: string;
  pref: string;
}

export default function Register() {
  const [prefectures, setPrefectures] = useState<PrefectureChoice[]>([]);
  const [successMessage, setSuccessMessage] = useState<string | null>(null); // State for feedback message
  const [errorMessage, setErrorMessage] = useState<string | null>(null); // State for error message

  useEffect(() => {
    // Fetch prefectures list
    axios.get("http://localhost:8000/api/prefectures/")
      .then(response => {
        if (Array.isArray(response.data)) {
          setPrefectures(response.data.map((pref) => ({
            value: pref.id,
            display_name: pref.name
          })));
        } else {
          console.error("Invalid response format", response.data);
        }
      })
      .catch(error => console.error("Error fetching prefectures:", error));
  }, []);

  const { register, handleSubmit, formState: { errors }, reset } = useForm<RegisterFormData>();

  const onSubmit = async (data: RegisterFormData) => {
    try {
      const response = await axios.post("http://localhost:8000/api/users/", data);  // Post registration data

      if (response.status === 201) {
        setSuccessMessage("Registration successful!");  // Set success message
        setErrorMessage(null);  // Clear any previous error messages
        reset();  // Reset form fields
      } else {
        setErrorMessage("Registration failed. Please try again.");
        setSuccessMessage(null);  // Clear any success messages
      }
    } catch (error) {
      console.error("Error during registration", error);
      setErrorMessage("Error during registration. Please try again.");
      setSuccessMessage(null);  // Clear any success messages
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Username:</label>
          <input
            {...register("username", { required: "Username is required", minLength: { value: 3, message: "Must be at least 3 characters" } })}
          />
          <p>{errors.username?.message}</p>
        </div>

        <div>
          <label>Email:</label>
          <input
            {...register("email", { required: "Email is required", pattern: { value: /^\S+@\S+$/, message: "Invalid email" } })}
          />
          <p>{errors.email?.message}</p>
        </div>

        <div>
          <label>Password:</label>
          <input
            type="password"
            {...register("password", {
              required: "Password is required",
              minLength: { value: 8, message: "Password must be at least 8 characters" },
              validate: (value: string) => {
                if (!/[A-Z]/.test(value)) return "Must contain an uppercase letter";
                if (!/[a-z]/.test(value)) return "Must contain a lowercase letter";
                if (!/\d/.test(value)) return "Must contain a number";
                return true;
              },
            })}
          />
          <p>{errors.password?.message}</p>
        </div>

        <div>
          <label>Phone:</label>
          <input
            {...register("tel", { pattern: { value: /^\d+$/, message: "Phone number must be digits only" } })}
          />
          <p>{errors.tel?.message}</p>
        </div>

        <div>
          <label>Prefecture:</label>
          <select {...register("pref", { required: "Please select a prefecture" })}>
            <option value="">Select Prefecture</option>
            {prefectures.map((pref) => (
              <option key={pref.value} value={pref.value}>{pref.display_name}</option>
            ))}
          </select>
          <p>{errors.pref?.message}</p>
        </div>

        <button type="submit">Register</button>
      </form>

      {/* Display success or error message */}
      {successMessage && <div style={{ color: 'green' }}>{successMessage}</div>}
      {errorMessage && <div style={{ color: 'red' }}>{errorMessage}</div>}
    </div>
  );
}
